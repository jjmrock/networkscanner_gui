
import customtkinter as ctk
from tkinter import ttk, filedialog
import socket, threading, queue, time, csv

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 3306: "MySQL", 8080: "HTTP-Alt"
}

class Scanner:
    def __init__(self):
        self.open_ports = []
        self.q = queue.Queue()
        self.stop_flag = False

    def worker(self, target):
        while not self.q.empty() and not self.stop_flag:
            port = self.q.get()
            try:
                s = socket.socket()
                s.settimeout(1)
                if s.connect_ex((target, port)) == 0:
                    service = COMMON_PORTS.get(port, "Unknown")
                    self.open_ports.append((port, service))
                s.close()
            except:
                pass
            self.q.task_done()

    def run(self, target, ports, threads=100, progress_cb=None):
        self.open_ports.clear()
        self.stop_flag = False

        for p in ports:
            self.q.put(p)

        total = len(ports)

        def updater():
            while not self.q.empty():
                done = total - self.q.qsize()
                if progress_cb:
                    progress_cb(done, total)
                time.sleep(0.2)

        threading.Thread(target=updater, daemon=True).start()

        workers = []
        for _ in range(threads):
            t = threading.Thread(target=self.worker, args=(target,))
            t.start()
            workers.append(t)

        for t in workers:
            t.join()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pro Port Scanner")
        self.geometry("1000x650")
        ctk.set_appearance_mode("dark")

        self.scanner = Scanner()
        self.create_ui()

    def create_ui(self):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x", pady=10, padx=10)

        self.target = ctk.CTkEntry(frame, placeholder_text="Target (IP or domain)")
        self.target.pack(side="left", padx=5, expand=True, fill="x")

        self.scan_type = ttk.Combobox(frame, values=["Quick", "Full"])
        self.scan_type.set("Quick")
        self.scan_type.pack(side="left", padx=5)

        ctk.CTkButton(frame, text="Scan", command=self.start_scan).pack(side="left", padx=5)
        ctk.CTkButton(frame, text="Stop", command=self.stop_scan).pack(side="left", padx=5)

        self.progress = ttk.Progressbar(self, length=500)
        self.progress.pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("Port", "Service", "Risk"), show="headings")
        for col in ("Port", "Service", "Risk"):
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        ctk.CTkButton(self, text="Export CSV", command=self.export).pack(pady=5)

    def get_ports(self):
        return range(1, 1025) if self.scan_type.get()=="Quick" else range(1, 65535)

    def risk(self, port):
        if port in [21,23]:
            return "⚠ Insecure"
        return "OK"

    def start_scan(self):
        target = self.target.get()
        ports = list(self.get_ports())
        self.tree.delete(*self.tree.get_children())

        def update(done, total):
            self.progress["value"] = (done/total)*100
            self.update_idletasks()

        def run():
            start = time.time()
            self.scanner.run(target, ports, threads=200, progress_cb=update)
            for p,s in self.scanner.open_ports:
                self.tree.insert("", "end", values=(p,s,self.risk(p)))
            print("Scan time:", time.time()-start)

        threading.Thread(target=run).start()

    def stop_scan(self):
        self.scanner.stop_flag = True

    def export(self):
        file = filedialog.asksaveasfilename(defaultextension=".csv")
        if not file: return
        with open(file,"w",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Port","Service"])
            writer.writerows(self.scanner.open_ports)

if __name__ == "__main__":
    App().mainloop()
