import argparse
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream


banner = """

         #####                                                
 #    # #     #  ####      ####  #      # ###### #    # ##### 
 #   #  #     # #         #    # #      # #      ##   #   #   
 ####    #####   ####     #      #      # #####  # #  #   #   
 #  #   #     #      #    #      #      # #      #  # #   #   
 #   #  #     # #    #    #    # #      # #      #   ##   #   
 #    #  #####   ####      ####  ###### # ###### #    #   #   

       #######                                                
          #    ######  ####  #####                            
          #    #      #        #                              
          #    #####   ####    #                              
          #    #           #   #                              
          #    #      #    #   #                              
          #    ######  ####    #                              


"""

def set_context(context_name ="minikube"):
    contexts, active_context = config.list_kube_config_contexts()
    if not contexts:
        print("Cannot find any context in kube-config file.")
        return
    try:
        config.load_kube_config(context=context_name)
    except config.config_exception.ConfigException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

def get_pod_env(pod, container):
    api = client.api.CoreV1Api()
    try:
        resp = api.read_namespaced_pod(name=pod,
                                       namespace='default')
    except ApiException as e:
        if e.status != 404:
            print("Unknown error: %s" % e)
            exit(1)

    exec_command = [
        '/bin/sh',
        '-c',
        'env' ]
    resp = stream(api.connect_get_namespaced_pod_exec,
                  name=pod,
                  namespace='default',
                  command=exec_command,
                  container=container,
                  stdout=True, tty=False)
    print("Response: " + resp)

def get_args():
    parser = argparse.ArgumentParser(description="Parse for pod and container(if any)")
    parser.add_argument("-p", "--pod")
    parser.add_argument("-c", "--container")
    args = parser.parse_args()
    print(args.pod, args.container)
    return ( args.pod, args.container)

if __name__ == "__main__":
    print(f"{banner}")
    (pod, container) = get_args()
    print(f"Get the env vars for pod ${pod} and container ${container}")
    set_context()
    get_pod_env(pod, container)
