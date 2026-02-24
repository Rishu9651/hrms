# HRMS Lite - Deployment Guide

This guide provides step-by-step instructions to deploy HRMS Lite to production using Render (backend) and Vercel (frontend).

## Prerequisites

- GitHub account
- Render account (free tier)
- Vercel account (free tier)
- Git installed locally
- Code pushed to GitHub

## Step 1: Push Code to GitHub

### 1.1 Create a New Repository on GitHub

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `hrms-lite`
3. Description: "Human Resource Management System - Full Stack Application"
4. Set to **Public** (required for free tier)
5. Do NOT initialize with README/gitignore (we have them)
6. Click "Create repository"

### 1.2 Push Local Code to GitHub

```bash
cd /path/to/hrms-lite

# Add GitHub remote
git remote add origin https://github.com/YOUR_USERNAME/hrms-lite.git

# Rename branch if needed (match GitHub)
git branch -M main

# Push to GitHub
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Step 2: Deploy Backend to Render

### 2.1 Create PostgreSQL Database on Render

1. Go to [render.com](https://render.com)
2. Sign up or login
3. Dashboard → Create → PostgreSQL
4. Configuration:
   - Name: `hrms-lite-db`
   - Database: `hrms`
   - User: `hrms_user` (or custom)
   - Region: Choose closest to you
   - Plan: Free (tier down to free if needed)
5. Click "Create Database"
6. Copy the **External Database URL** (save for later)

### 2.2 Deploy Backend Service

1. Dashboard → New → Web Service
2. Select "Public Git Repository"
3. Enter connection string:
   ```
   https://github.com/YOUR_USERNAME/hrms-lite.git
   ```
4. Configuration:
   - **Name**: `hrms-lite-api`
   - **Region**: Same as database (important for performance)
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: 
     ```
     pip install -r hrms-lite-backend/requirements.txt
     ```
   - **Start Command**: 
     ```
     cd hrms-lite-backend && uvicorn main:app --host 0.0.0.0 --port $PORT
     ```
5. Click "Advanced" and add Environment Variables:
   
   | Key | Value |
   |-----|-------|
   | `DATABASE_URL` | Paste the PostgreSQL URL from step 2.1 |
   | `ENVIRONMENT` | `production` |
   | `DEBUG` | `false` |

6. Click "Deploy Web Service"

### 2.3 Verify Backend Deployment

Wait 5-10 minutes for deployment to complete.

Once live, test endpoints:

```bash
# Replace with your Render URL
BACKEND_URL="https://hrms-lite-api.onrender.com"

# Health check
curl $BACKEND_URL/health

# API documentation
open $BACKEND_URL/docs

# Get employees
curl $BACKEND_URL/api/employees
```

**Note**: Save your backend URL:
```
https://hrms-lite-api.onrender.com
```

## Step 3: Deploy Frontend to Vercel

### 3.1 Connect Repository to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Sign up or login with GitHub
3. Click "Import Project"
4. Paste repository URL: `https://github.com/YOUR_USERNAME/hrms-lite`
5. Click "Continue"

### 3.2 Configure Frontend Project

1. **Framework Preset**: Select `Vite`
2. **Project Settings**:
   - **Root Directory**: `hrms-lite-frontend`
   - **Build Command**: `npm run build` (should auto-fill)
   - **Output Directory**: `dist` (should auto-fill)
3. **Environment Variables**:
   - Add new variable:
     - Key: `VITE_API_URL`
     - Value: `https://hrms-lite-api.onrender.com/api` (your backend URL from section 2.3)

### 3.3 Deploy

Click "Deploy"

Wait for deployment to complete (usually 2-5 minutes).

### 3.4 Verify Frontend Deployment

Once deployed, Vercel will provide your frontend URL:
```
https://hrms-lite.vercel.app
```

Test the application:
- Visit the URL above
- Try adding an employee
- Try marking attendance
- Verify no console errors

## Step 4: Update Configuration Files

### 4.1 Update .env.production in Frontend

If you haven't committed the production .env, add it:

```bash
cd hrms-lite-frontend

# Create production env file (don't commit this to git)
echo "VITE_API_URL=https://hrms-lite-api.onrender.com/api" > .env.production

# OR update Vercel settings directly through dashboard
```

### 4.2 Verify CORS Settings

The backend CORS is open to all origins (`allow_origins=["*"]`). 

For production, you should customize this in `hrms-lite-backend/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://hrms-lite.vercel.app"],  # Specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Then redeploy backend.

## Deployment Checklist

### Backend (Render)

- [ ] PostgreSQL database created
- [ ] Environment variables set:
  - [ ] `DATABASE_URL` with PostgreSQL URL
  - [ ] `ENVIRONMENT=production`
  - [ ] `DEBUG=false`
- [ ] Build command configured
- [ ] Start command configured
- [ ] Root directory set to `hrms-lite-backend` (if in subdirectory)
- [ ] Health check endpoint `/health` responding
- [ ] API docs accessible at `/docs`

### Frontend (Vercel)

- [ ] Repository connected to Vercel
- [ ] Root directory set to `hrms-lite-frontend`
- [ ] Build and output directories correct
- [ ] Environment variable `VITE_API_URL` set to backend URL
- [ ] Frontend loads without errors
- [ ] API calls successful
- [ ] Employee create/edit/delete works
- [ ] Attendance marking works

### Code Quality

- [ ] Git repository is public
- [ ] README.md is comprehensive
- [ ] .gitignore prevents committing node_modules, venv
- [ ] No hardcoded URLs in code
- [ ] All environment variables documented

## Troubleshooting

### Backend Issues

**Backend won't start**
- Check build logs in Render dashboard
- Verify all dependencies in requirements.txt
- Ensure `main.py` is in the correct directory
- Check that the start command is correct

**Database connection error**
- Verify PostgreSQL URL is correct
- Check database credentials
- Ensure database exists and user has permissions
- Test URL with: `psql <DATABASE_URL>`

**CORS errors**
- Check that CORS middleware is enabled
- Verify frontend URL is allowed
- Check `allow_origins` configuration

### Frontend Issues

**Blank page or build error**
- Check build logs in Vercel
- Verify root directory is `hrms-lite-frontend`
- Ensure `package.json` exists in root directory
- Check for TypeScript/JavaScript errors

**API calls failing**
- Verify `VITE_API_URL` environment variable is set
- Ensure backend is running and accessible
- Check browser console for CORS errors
- Test API directly: `curl https://hrms-lite-api.onrender.com/health`

**Data not persisting**
- Verify backend is using PostgreSQL (not SQLite)
- Check database connection string
- Verify database hasn't reached connection limit

## Performance Optimization

### Backend

1. **Database**: Use indexes on frequently queried columns (done in models)
2. **Caching**: Consider Redis for repeated queries
3. **Monitoring**: Use Render dashboard to monitor CPU/memory

### Frontend

1. **Build optimization**: Vite automatically optimizes for production
2. **Code splitting**: React lazy loading (not needed for small app)
3. **Image optimization**: No large images in this app

## Security Checklist

- [ ] `DEBUG=false` in production
- [ ] CORS configured for specific frontend URL
- [ ] No sensitive data in environment variables (use secrets manager if needed)
- [ ] API validates all input (server-side)
- [ ] No SQL injection possible (using SQLAlchemy ORM)
- [ ] HTTPS enabled (default on Render/Vercel)
- [ ] Database backups configured (Render provides automated backups)

## Monitoring & Maintenance

### Backend (Render)

Monitor in Render dashboard:
- CPU usage
- Memory usage
- Disk usage (database)
- Failed requests
- Build history

### Frontend (Vercel)

Monitor in Vercel analytics:
- Page load time
- Core Web Vitals
- Error rate
- Geographic distribution

## Scaling for Production

If usage grows:

1. **Database**: Upgrade to paid PostgreSQL plan
2. **Backend**: Scale to multiple instances on Render
3. **Frontend**: Already on global CDN (Vercel)
4. **Caching**: Add Redis for performance
5. **Logging**: Add structured logging service
6. **Monitoring**: Use Sentry for error tracking

## Rollback Procedure

### Backend
```bash
git revert <commit-hash>
git push origin main
# Render will auto-redeploy
```

### Frontend
Use Vercel dashboard → Deployments → Select previous version → Promote to Production

## Domain Configuration (Optional)

### Add Custom Domain

**Vercel**:
1. Dashboard → Project → Settings → Domains
2. Add custom domain
3. Configure DNS records (Vercel provides instructions)

**Render**:
1. Dashboard → Backend Service → Settings → Custom Domain
2. Add domain
3. Configure DNS records

## Next Steps

1. ✅ Deploy code to production
2. ✅ Test all functionality
3. ✅ Share live URLs with stakeholders
4. ✅ Monitor performance
5. ✅ Plan future improvements
6. Consider: Authentication, Analytics, Backup Strategy

## Support & Resources

- [Render Documentation](https://render.com/docs)
- [Vercel Documentation](https://vercel.com/docs)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [React Production Build](https://react.dev/learn/start-a-new-react-project)

---

**Deployment Date**: February 24, 2026
**Status**: Production Ready ✅
