# Build-in modules
import logging
import threading

# Added modules
from ttictoc import TicToc

# Project modules

# Print in file
# logging.basicConfig(filename='logs.log',
#                     filemode='w',
#                     level=logging.INFO,
#                     format='%(asctime)s | %(process)d | %(name)s | %(levelname)s:  %(message)s',
#                     datefmt='%d/%b/%Y - %H:%M:%S')

# Print in software terminal
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s | %(process)d | %(name)s | %(levelname)s:  %(message)s',
                    datefmt='%d/%b/%Y - %H:%M:%S')

logger = logging.getLogger(__name__)


class ElapsedTime(object):
    """
Measure the elapsed time between some "object.t" and "object.elapsed".
    """

    def __init__(self):
        self.t = TicToc('digest')

    def elapsed(self):
        self.t.toc()
        _elapsed = self.t.elapsed
        d = timedelta(seconds=_elapsed)
        logger.info('< {} >'.format(d))


class ThreadingProcessQueue(object):
    """
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval):
        """
        Constructor
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=(self.interval,), name='Thread_name')
        thread.daemon = True  # Daemonize thread
        thread.start()  # Start the execution

    def run(self, interval):
        """ Method that runs forever """
        while True:
            try:
                time.sleep(interval)

            except ThreadError as e:
                logger.exception('{}'.format(e))

            finally:
                pass


def application():
    """" All application has its initialization from here """
    logging.info('Main application is running!')
