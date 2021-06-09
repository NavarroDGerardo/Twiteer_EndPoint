# Twiteer_EndPoint

# Team
Jorge Iván Morales González     A01652650
Alan Rodrigo Mendoza Aguilar    A01339625
In Joong Kim					          A01336967
Diego Gerardo Navarro González  A01338941

# Deployment
## Docker compose deployment
```bash
docker-compose up
```
NOTE: Make sure to delete docker containers before try kubernetes deployment

## Kubernetes deployment
```bash
kubectl apply -f kubernetes
```

# Extra
## Docker compose to kurbenetes
Install kompose and use the following command
```bash
kompose convert
```
or
```bash
kompose.exe convert
```
