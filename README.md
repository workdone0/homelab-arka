# Homelab Arka

A lightweight Kubernetes setup for running self-hosted media services in a homelab environment.  
This project includes manifests for deploying **Jellyfin** (media server) and **Transmission** (torrent client), with persistent storage and namespace management.

---

## Features
- 📺 **Jellyfin** – Open-source media server for streaming movies, TV shows, and music.  
- 📥 **Transmission** – Lightweight torrent client for downloading media.  
- 📂 **Persistent Volumes** – Kubernetes PV/PVC configurations for durable storage.  
- 🗂 **Namespace Isolation** – Dedicated `media` namespace for organizing deployments.

---

## Project Structure
```
homelab-arka/
├── jellyfin/
│   ├── deployment.yaml      # Jellyfin Deployment & Service
│   ├── pv-pvc.yaml          # Persistent Volume + PVC for Jellyfin
│
├── transmission/
│   ├── deployment.yaml      # Transmission Deployment & Service
│   ├── pv-pvc.yaml          # Persistent Volume + PVC for Transmission
│
└── utils/
    └── namespace-media.yaml # Namespace definition for media services
```

---

## Prerequisites
- A running **Kubernetes cluster** (K3s, Minikube, MicroK8s, or bare metal).  
- `kubectl` configured to access your cluster.  
- Storage provisioner available (e.g., local-path, NFS, or cloud storage class).  

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/workdone0/homelab-arka.git
   cd homelab-arka
   ```

2. Create the `media` namespace:
   ```bash
   kubectl apply -f utils/namespace-media.yaml
   ```

3. Deploy **Jellyfin**:
   ```bash
   kubectl apply -f jellyfin/pv-pvc.yaml
   kubectl apply -f jellyfin/deployment.yaml
   ```

4. Deploy **Transmission**:
   ```bash
   kubectl apply -f transmission/pv-pvc.yaml
   kubectl apply -f transmission/deployment.yaml
   ```

---

## Usage
- **Jellyfin**: Access via the exposed service (LoadBalancer, NodePort, or Ingress depending on your setup).  
- **Transmission**: Access the web UI the same way.  

Check running pods:
```bash
kubectl get pods -n media
```

---

## Customization
- Update storage paths in `pv-pvc.yaml` to match your environment.  
- Modify container images or resource requests in `deployment.yaml`.  
- Add Ingress resources if you want domain-based access.  

---

## Contributing
Pull requests and suggestions are welcome!  
If you want to add more services (e.g., Sonarr, Radarr, Plex), feel free to fork and extend.

---

## License
This project is licensed under the MIT License.  
