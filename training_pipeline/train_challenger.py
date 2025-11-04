from prefect import flow, task

@task
def say_hi():
    print("✅ Prefect task ok")

@flow(name="training_challenger_flow")
def training_challenger_flow():
    say_hi()

if __name__ == "__main__":
    training_challenger_flow()
