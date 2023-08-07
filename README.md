# `logging` Module's Best Practices in Deep Learning Projects

## Introduction

This document describes the best practices for using the `logging` module in Deep Learning projects. As we know, the `logging` module is a powerful tool for debugging and monitoring the execution of a program. However, it is not easy to use it properly, especially in a large and complex deep learning projects with multiple files and hierarchies. In such projects, it is very important to have a consistent and well-organized logging system, which can help us to debug and monitor the program efficiently. Also, we usually don't need to consider the overflow of the log files, because the log files are usually small in size for such projects, which gives us less pressure to manage the log files. Certainly, although I call it "best practices", it is not the only way to use the `logging` module, but it is a good way to use it in deep learning projects for beginners to `logging` module.

- This project gives an example of how to use the `logging` module in a deep learning project, you can use it as a template for your own project. 
- It supports: 
  - Logging to both console and file.
  - Parse command line arguments to set the logging level.
  - Give each module its own logger with the module's name.
  - A proper format for the log messages for deep learning projects, which includes the datetime, module name, message level, line number, and the message itself.
- With minimal effort, you can use it in your own project by replacing your `print` statements with statements like `logger.info` or `logger.debug`.
- It is based on the [Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html), [Python Logging HOWTO](https://docs.python.org/3/howto/logging.html), and the [Python Logging Best Practices: The Ultimate Guide](https://coralogix.com/blog/python-logging-best-practices-tips/).

Have fun!