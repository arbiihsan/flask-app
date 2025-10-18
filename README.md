# Flask App by Arbi M Ihsan

This is the documentation of my simple Flask App project. Including screenshots for some of the process. This app containerized with Docker and deployed on DigitalOcean Kubernetes using CI/CD automation with GitHub Actions.

## Endpoints

This Flask App provides 3 REST API endpoints:

- `GET /` - Arbi's Flask App message with timestamp
- `GET /health` - Health check endpoint
- `GET /api/info` - App info (version, environment)


## Running the Application

### 1. Dev mode

```bash
pip install -r requirements.txt

python app.py
```

locally, the app will be available at: `http://localhost:5000`

### 2. Test the Endpoints

```bash
curl http://localhost:5000/

curl http://localhost:5000/health

curl http://localhost:5000/api/info
```

## Docker Configuration

### Build Docker Image Locally

```bash
docker build -t arbiihsan/flask-app:latest .

docker run -p 5000:5000 arbiihsan/flask-app:latest
```

### Push to Docker Hub (Manual)

```bash
docker login

docker push arbiihsan/flask-app:latest
```

## Kubernetes Deployment

### Setup DigitalOcean Kubernetes

1. **Get cluster credentials:**

```bash
doctl auth init

doctl kubernetes cluster kubeconfig save flask-app
```

2. **Verify connection:**

```bash
kubectl cluster-info

kubectl get nodes
```

### Deploy to Kubernetes (Manual)

#### ClusterIP Service (Internal Access)

```bash
kubectl apply -f deployment.yaml

kubectl apply -f service.yaml

kubectl get deployments

kubectl get pods

kubectl get services
```

#### Ingress (Domain Access)

install NGINX Ingress Controller on DigitalOcean:

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/cloud/deploy.yaml
```

apply the ingress:

```bash
kubectl apply -f deployment.yaml

kubectl apply -f service.yaml

kubectl apply -f ingress.yaml

kubectl get ingress flask-app-ingress
```

## CI/CD Pipeline

Github Actions workflow:
1. Build the Docker image and Push to Docker Hub
2. Deploy to DigitalOcean Kubernetes cluster
3. Verify deployment status

## Access the App

### Via Ingress (External via Domain)

Access at: http://arbi-flask.duckdns.org
```bash
curl http://arbi-flask.duckdns.org

curl http://arbi-flask.duckdns.org/health

curl http://arbi-flask.duckdns.org/api/info
```

## Screenshots

### Build docker image locally and push
![plot](./screenshots/screenshot_build%20docker.png)
![plot](./screenshots/screenshot_push%20docker.png)

### CI/CD pipeline jobs completed
![plot](./screenshots/screenshot_cicd%20pipeline.png)

### Verify new pods are running
![plot](./screenshots/Screenshot%202025-10-19%20034420.png)

### Get the Ingress Controller's LoadBalancer IP
![plot](./screenshots/Screenshot%202025-10-19%20034814.png)

### Deployed API Usage
![plot](./screenshots/Screenshot%202025-10-19%20020353.png)
![plot](./screenshots/Screenshot%202025-10-19%20020415.png)
![plot](./screenshots/Screenshot%202025-10-19%20020452.png)


## Additional Info
**Created by:** Arbi M Ihsan  
**Docker Hub:** [arbiihsan/flask-app](https://hub.docker.com/r/arbiihsan/flask-app)
