from tools.lib.route import Route
from tools.lib.logreader import LogReader

r = Route("61c01eb07512b130|2023-06-04--10-57-47")

# get a list of paths for the route's rlog files
print(r.log_paths())

# and road camera (fcamera.hevc) files
print(r.camera_paths())

# setup a LogReader to read the route's first rlog
lr = LogReader(r.log_paths()[0])

# print out all the messages in the log
import codecs
codecs.register_error("strict", codecs.backslashreplace_errors)
with open("./output.txt", "w") as file:
    for msg in lr:
        file.write(str(msg) + "\n")
# for msg in lr:
#   print(msg)

# setup a LogReader for the route's second qlog
lr = LogReader(r.log_paths()[1])

# print all the steering angles values from the log
# for msg in lr:
#   if msg.which() == "carState":
#     print(msg.carState.steeringAngleDeg)