# Azure Deployment Guide

This project is designed to run as one web app: the FastAPI backend serves the UI routes and the API in the same process.

## Current Proof Of Concept Scope

This deployment is a single website, not split services.

Current work is citation verification on top of the already-working metadata and chunking layers.

Do not re-ingest the 300-case review list yet; that is a later step after citation behavior is stable.

## Recommended Azure setup

Use:
- Azure Container Apps, or Azure App Service for Containers
- Azure Database for PostgreSQL Flexible Server
- Azure Key Vault or App Settings for secrets

## What to deploy

Build one Docker image from the repository root. The image runs `backend.main:app`, which serves:
- the API
- the citation-pass UI
- the case-reader / citation-map pages

This is the only website users should view during the proof of concept.

## Environment variables

Set these in Azure:
- `DATABASE_URL` pointing to Azure PostgreSQL
- `OPENAI_API_KEY` if you use live OpenAI features
- any other app-specific secrets already used locally

If you prefer individual PostgreSQL fields, keep the existing `POSTGRES_*` variables and let the app assemble the connection.

## Azure PostgreSQL

Create a PostgreSQL Flexible Server and database, then set `DATABASE_URL` to the Azure connection string.

Example format:

```text
postgresql://USERNAME:PASSWORD@SERVER.postgres.database.azure.com:5432/DATABASE?sslmode=require
```

## Build and run locally with Docker

```powershell
docker build -t aicaselibrary .
docker run --rm -p 8000:8000 --env-file .env aicaselibrary
```

## Azure Container Apps path

1. Create the container app environment.
2. Push the image to Azure Container Registry, Docker Hub, or GHCR.
3. Create the container app from that image.
4. Add the app settings above.
5. Open the app URL and use the built-in UI pages.

## GitHub Actions automation

The repository includes [.github/workflows/azure-deploy.yml](../.github/workflows/azure-deploy.yml) for automated deploys from `main`.

Configure these GitHub repository variables:
- `AZURE_RESOURCE_GROUP`
- `AZURE_CONTAINER_APP_NAME`
- `ACR_NAME`

Configure these GitHub repository secrets:
- `AZURE_CLIENT_ID`
- `AZURE_TENANT_ID`
- `AZURE_SUBSCRIPTION_ID`

The Azure service principal behind the OIDC login needs permission to push to the ACR and update the Container App.

## Verification

After deployment, verify these URLs:
- `/` for the backend health response
- `/citation-pass` for live citation extraction
- `/case-reader` for case browsing
- `/docs` for the API docs

## Notes

- The UI is already served by the backend, so you do not need a separate frontend deployment.
- The app must run behind a public HTTPS endpoint if you want external access.