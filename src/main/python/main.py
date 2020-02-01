import sys
from fbs_runtime.application_context.PySide2 import ApplicationContext
from run_it.main_widget import MainWidget


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWidget()
    window.resize(1200, 800)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
