# logger.py

class Logger:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self.log_file = open(log_file_path, 'w')
        self.warning_msgs = []
        self.error_msgs = []
        self.info_msgs = []
    
    def log(self, level, message):
        if level == "WARNING":
            self.warning_msgs.append(message)
        elif level == "ERROR":
            self.error_msgs.append(message)
        elif level == "INFO":
            self.info_msgs.append(message)
    
    def write_log(self):
        self.log_file.write("### Warnings\n")
        for msg in self.warning_msgs:
            self.log_file.write(f"- {msg}\n")
        self.log_file.write("\n### Errors\n")
        for msg in self.error_msgs:
            self.log_file.write(f"- {msg}\n")
        self.log_file.write("\n### Info\n")
        for msg in self.info_msgs:
            self.log_file.write(f"- {msg}\n")
        self.log_file.write("\n")
        self.log_file.write("### End of Log\n")
    
    def close(self):
        self.log_file.close()