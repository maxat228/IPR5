# Лабораторная работа №5: Основы Kubernetes (k8s)

Развёртывание контейнеризированного приложения «Калькулятор» в Kubernetes.

## Что это

Два сервиса:

- **backend** (`calculator:2.0.0`) — Python HTTP-сервер на порту 8080. Считает выражения через класс `Calculator`.
- **frontend** (`calculator-frontend:1.0.0`) — Python HTTP-сервер на порту 80. Отдаёт `index.html` и проксирует `/api/*` на backend.

Связь: frontend → `backend-service:8080` через DNS Kubernetes.

## Структура проекта
```
IPRLab5/
├── Dockerfile                     # backend-образ
├── server.py                      # backend HTTP-сервер (порт 8080)
├── requirements.txt
├── src/
│   ├── init.py
│   ├── calculator.py              # класс Calculator
│   └── main.py                    # CLI-версия
├── frontend/
│   ├── Dockerfile                 # frontend-образ
│   ├── server.py                  # прокси на backend-service:8080
│   └── index.html                 # UI калькулятора
├── k8s-manifests/
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   └── frontend-service.yaml
├── tests/
├── .gitignore
├── LICENSE
└── README.md
```

## Сборка образов
```
bash
docker build -t calculator:2.0.0 .

cd frontend
docker build -t calculator-frontend:1.0.0 .
cd ..
```

## Развёртывание в Kubernetes

Требуется работающий кластер (Minikube, kind или Docker Desktop Kubernetes).

```
kubectl apply -f k8s-manifests/namespace.yaml
kubectl apply -f k8s-manifests/configmap.yaml
kubectl apply -f k8s-manifests/secret.yaml
kubectl apply -f k8s-manifests/backend-deployment.yaml
kubectl apply -f k8s-manifests/backend-service.yaml
kubectl apply -f k8s-manifests/frontend-deployment.yaml
kubectl apply -f k8s-manifests/frontend-service.yaml
```

Если кластер — Minikube/kind, образы нужно предварительно загрузить:

```
minikube image load calculator:2.0.0
minikube image load calculator-frontend:1.0.0
```

## Проверка

```
kubectl get nodes
kubectl get pods -n lab5
kubectl get svc -n lab5
kubectl get configmap,secret -n lab5
```

Все поды должны быть в статусе Running. Доступ к приложению Docker Desktop (NodePort): http://localhost:30080

## Minikube / kind (port-forward)

```
kubectl port-forward service/frontend-service 8080:80 -n lab5
```

Затем открыть http://localhost:8080.

## API

Метод Путь Описание
GET /health Проверка живости ({"status": "healthy"})
GET /api/calc?op=add&a=2&b=3 Вычисление ({"result": 5.0})

Доступные операции: add, subtract, multiply, divide, power.

## Масштабирование

### Увеличить количество backend-подов до 5
```
kubectl scale deployment backend --replicas=5 -n lab5
```

### Вернуть обратно
```
kubectl scale deployment backend --replicas=2 -n lab5
```

## Rolling update

```
kubectl set image deployment/backend backend=calculator:2.0.0 -n lab5
kubectl rollout status deployment/backend -n lab5
kubectl rollout undo deployment/backend -n lab5
```

## Конфигурация

· ConfigMap app-config — обычные настройки (APP_ENV, LOG_LEVEL).
· Secret app-secret — чувствительные данные (API_KEY).

Подключаются в backend-deployment.yaml через envFrom.

## Очистка

```
kubectl delete namespace lab5
```

## Технологии

· Python 3.12
· Docker
· Kubernetes (Minikube / Docker Desktop / kind)
· kubectl
