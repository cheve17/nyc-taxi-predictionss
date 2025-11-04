from prefect import flow, task, get_run_logger

@task
def say_hi():
    logger = get_run_logger()
    logger.info("Prefect task ok")  # SOLO ASCII

@flow(name="training_challenger_flow")
def training_challenger_flow():
    say_hi()

if __name__ == "__main__":
    training_challenger_flow()
