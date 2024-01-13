import logging
import unittest
from queue import Queue
from unittest.mock import patch

from threadpool import ThreadPool, ThreadPoolWorker


class TestThreadPool(unittest.TestCase):
    def test_error_logging(self):
        # Create a ThreadPool instance with a single worker thread
        thread_pool = ThreadPool(num_threads=1)

        # Create a mock function that raises an exception
        def mock_function():
            raise ValueError("Test exception")

        # Enqueue the mock function to the ThreadPool
        thread_pool.enqueue(mock_function)

        # Patch the logging.error method to capture the logged message
        with patch.object(logging, "error") as mock_error:
            # Wait for the task to complete
            thread_pool.wait()

            # Verify that the error was logged correctly
            mock_error.assert_called_with(
                "Args %s %s %s", mock_function, (), {}
            )

    # Add more test cases here to cover other scenarios and edge cases


if __name__ == "__main__":
    unittest.main()
