SECTION 1:
---------
    # What's kibana and why we use it ?
        - Kibana is an open source browser based visualization tool.
        - Searching, viewing, and visualizing data indexed in Elasticsearch and analyzing the data
        - By using data Creation of bar charts, pie charts, tables, histograms, and maps
        - Kibana works in sync with Elasticsearch and Logstash which together forms the so called ELK.
        - A dashboard view combines these visual elements to then be shared via browser.
        - Kibana used for Infrastructure metrics and container monitoring
        - Application performance monitoring (APM)
        - Geospatial data analysis and visualization
        - Monitoring, managing, and securing an Elastic Stack instance via web interface.
        - Kibana dashboard is a collection of charts, graphs, metrics, searches, and maps that have been    collected together onto a single pane.

SECTION 2:
---------
    # Deploying kibana using Dockers :
        - Docker images for Kibana are available from the Elastic Docker registry
        - Before pull Docker Image (Kibana image) We have to create the Docker network

        - Docker network creation
            docker network create <Network_Name>

        1. Docker Image name
            docker pull docker.elastic.co/kibana/kibana:8.5.0
            
        2. Running Docker Container
            docker run --name <kibana> --net <Network_Name> -p 5601:5601 docker.elastic.co/kibana/kibana:8.5.0

        - Kibana default port number is 5601
        - We can access the kibana UI Access using localhost:5601 or VM_IP:5601        
        
SECTION 3:
---------
    # Deploying kibana using Kubernetes :
        - First we have to create name space for kibana

        - Name Space create by using below command
            kubectl create namespace <namespace_name>
        
        - Check name space created or not by Using below command
            kubectl get namespace        

        1. Deployment Spec
            - We can create Deployment yml file for kibana
                vi deployment.yml

            - To deploy the kibana by using below command specified namespace
                kubectl create -f service.yml -n <Namespace>

        2. Service Spec
            - We can create Service yml file for kibana
                vi service.yml

            - To deploy the kibana by using below command specified namespace
                kubectl create -f service.yml -n <Name_space>

            - Kibana UI Access using localhost:port or VM_IP:port

        3. kubectl commands for debug
            - Describe the pod by using below command
                kubectl describe  pod <pod-name> -n <namespace-name>

            - Edit pod by using below command
                kubectl edit  pod <pod-name> -n <namespace-name>

            - Describe the service by using below command
                kubectl describe  svc <svc-name> -n <namespace-name>  

            - Edit Service by using below command
                kubectl edit  svc <svc-name> -n <namespace-name>
    
               
SECTION 4:
---------
    # Deploying kibana using HELM
        1. HELM Charts
        2. HELM commands for bring-up
        3. HELM commands for debug

SECTION 5:
---------
    # Verification post installation
        1. Access kibana in UI

        2. CREATE/DELETE/UPDATE Indexes
            CREATE : 

        3. kubectl commands for kibana

SECTION 6:
---------
    # kibana UI Access
        1. UI Link

SECTION 7:
---------
    # REST API Commands for all CRUD
        - Hello

SECTION 8:
----------
# Kibana deployment yml file
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kibana
  namespace: kibana
  labels:
    app: kibana
    kubernetes.io/cluster-service: "true"
    addonmanager.kubernetes.io/mode: Reconcile
spec:
  replicas: 1
  selector:
    matchLabels:
      app: kibana
  template:
    metadata:
      labels:
        app: kibana
      annotations:
        seccomp.security.alpha.kubernetes.io/pod: 'docker/default'
    spec:
      containers:
      - name: kibana
        image: docker.elastic.co/kibana/kibana-oss:6.5.4
        resources:
          # need more cpu upon initialization, therefore burstable class
          limits:
            cpu: 1000m
          requests:
            cpu: 100m
        env:
          - name: ELASTICSEARCH_URL
            value: http://10.74.190.127:31931/
        ports:
        - containerPort: 5601
          name: ui
          protocol: TCP

# Kibana Service yml file
apiVersion: v1
kind: Service
metadata:
  name: kibana
  namespace: kibana
  labels:
    app: kibana
    kubernetes.io/cluster-service: "true"
    addonmanager.kubernetes.io/mode: Reconcile
    kubernetes.io/name: "Kibana"
spec:
  type: NodePort
  ports:
  - port: 5601
    protocol: TCP
    targetPort: ui
    nodePort: 31336
  selector:
    app: kibana          


SECTION 9:
---------
    # References
        - https://www.youtube.com/watch?v=pL_0qKxIWZE
        - https://www.elastic.co/guide/en/kibana/current/docker.html
        - https://dev.to/elastic/performing-crud-operations-with-elasticsearch-kibana-50ka

