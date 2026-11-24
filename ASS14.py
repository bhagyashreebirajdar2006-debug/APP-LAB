
import logging

# Configure logging
logging.basicConfig(
    filename="program.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    logging.debug("Program started")

    a = 10
    b = 2

    logging.info("Performing division")

    result = a / b

    print("Result:", result)

    logging.info("Division completed successfully")

    # Generate an exception
    x = 10
    y = 0
    result = x / y

except Exception:
    logging.exception("An error occurred")

finally:
    logging.info("Program execution completed")
