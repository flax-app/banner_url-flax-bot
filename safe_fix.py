import psutil

class SafeSystemStats:
    @staticmethod
    def cpu():
        try:
            cores = psutil.cpu_count(logical=False)
            threads = psutil.cpu_count(logical=True)
            load = psutil.cpu_percent(interval=0.1)
            return f"{cores} ({threads}) cores; {load}%"
        except:
            return "N/A"