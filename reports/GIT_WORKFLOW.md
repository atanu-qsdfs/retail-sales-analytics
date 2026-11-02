# Git workflow (PowerShell)
Run commands inside this project folder.
```powershell
git init
git branch -M main
git add README.md requirements.txt .gitignore
git commit -m "chore: add project structure and documentation"
```
Create an empty GitHub repository named `retail-sales-analytics`, then connect it:
```powershell
git remote add origin https://github.com/YOUR-USERNAME/retail-sales-analytics.git
git push -u origin main
```
After adding the pipeline:
```powershell
git add src
git commit -m "feat: add data cleaning and EDA pipeline"
git push
```
After analysis and report:
```powershell
git add data/processed visuals powerbi reports presentation
git commit -m "feat: add analysis outputs and dashboard documentation"
git push
```
Practice pull: `git pull origin main`. Replace `YOUR-USERNAME` with your GitHub username. Do not commit secrets or the large original XLSX.
