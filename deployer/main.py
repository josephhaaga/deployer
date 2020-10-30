import configparser
import importlib


def main() -> int:
    config = configparser.ConfigParser()
    config.read("flow.conf")
    flow_module, flow_object = config["prefect"]["flow"].split(":")
    mod = importlib.import_module(flow_module)
    flow = getattr(mod, flow_object)
    deploy(flow)
    return 0


def deploy(f):
    print(f"Deploying flow {flow}")


if __name__ == "__main__":
    exit(main())
