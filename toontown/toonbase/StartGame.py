import traceback



try:
    run()
except:
    traceback_info = traceback.format_exc()
else:
    traceback_info = 'Program crashed but no error was found'
finally:
    print(traceback_info)