# Guía para publicar SmartDesk AI por ramas

> Ejecutar estos pasos con Git Bash o PowerShell desde la carpeta raíz del proyecto.

## 1. Configurar identidad Git
```bash
git config --global user.name "TU NOMBRE"
git config --global user.email "TU_CORREO_GITHUB"
```

## 2. Crear el repositorio local
```bash
git init
git branch -M main
git add .gitignore README.md BRANCH_PLAN.md GUIA_GITHUB.md
git commit -m "chore: initialize SmartDesk AI repository"
```

## 3. Crear rama develop
```bash
git checkout -b develop
```

## 4. Rama de especificaciones Kiro
```bash
git checkout -b feature/kiro-specs
git add .kiro
git commit -m "docs: add Kiro requirements specification"
git commit --allow-empty -m "docs: add Kiro design and implementation tasks"
git checkout develop
git merge --no-ff feature/kiro-specs -m "merge: integrate Kiro specifications"
```

## 5. Rama backend
```bash
git checkout -b feature/backend-api
git add backend/app backend/requirements.txt
git commit -m "feat: implement ticket API and persistence"
git checkout develop
git merge --no-ff feature/backend-api -m "merge: integrate backend API"
```

## 6. Rama IA
```bash
git checkout -b feature/ai-classifier
git add data backend/app/services/classifier.py
git commit -m "feat: implement AI classification service"
git checkout develop
git merge --no-ff feature/ai-classifier -m "merge: integrate AI classifier"
```

## 7. Rama frontend
```bash
git checkout -b feature/frontend
git add frontend
git commit -m "feat: implement React ticket interface"
git checkout develop
git merge --no-ff feature/frontend -m "merge: integrate frontend"
```

## 8. Rama de pruebas
```bash
git checkout -b feature/tests
git add backend/tests pytest.ini .github/workflows/tests.yml
git commit -m "test: add unit and integration tests"
git checkout develop
git merge --no-ff feature/tests -m "merge: integrate automated tests"
```

## 9. Rama de documentación
```bash
git checkout -b docs/architecture
git add docs .github/pull_request_template.md README.md
git commit -m "docs: complete architecture and project documentation"
git checkout develop
git merge --no-ff docs/architecture -m "merge: integrate documentation"
```

## 10. Integrar develop en main
```bash
git checkout main
git merge --no-ff develop -m "release: SmartDesk AI v1.0"
```

## 11. Conectar con GitHub
Primero crear en GitHub un repositorio vacío llamado `smartdesk-ai` sin README ni .gitignore adicionales.

Luego:
```bash
git remote add origin https://github.com/TU_USUARIO/smartdesk-ai.git
git push -u origin main
git push -u origin develop
git push -u origin feature/kiro-specs
git push -u origin feature/backend-api
git push -u origin feature/ai-classifier
git push -u origin feature/frontend
git push -u origin feature/tests
git push -u origin docs/architecture
```

## Importante sobre Pull Requests
Para que GitHub muestre Pull Requests reales como evidencia, lo correcto es NO fusionar localmente las ramas antes de crear los PR. En la entrega definitiva conviene seguir esta variante:

1. Crear y publicar cada rama.
2. Abrir Pull Request de cada `feature/*` hacia `develop`.
3. Fusionar desde GitHub.
4. Finalmente abrir `develop` hacia `main`.

La secuencia será:
```text
feature/kiro-specs       -> develop
feature/backend-api      -> develop
feature/ai-classifier    -> develop
feature/frontend         -> develop
feature/tests            -> develop
docs/architecture        -> develop
develop                  -> main
```

De esta manera GitHub mostrará ramas, commits y Pull Requests de forma similar al ejemplo de la Segunda Instancia.
