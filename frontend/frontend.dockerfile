FROM node:20-slim as base

ENV NODE_ENV=production

WORKDIR /src

# Build
FROM base as build

COPY package.json .
RUN npm install --production=false

COPY . .

RUN npm run build
RUN npm prune

# Run
FROM base

ENV PORT=3000

COPY --from=build /src/.output /src/.output
CMD [ "node", ".output/server/index.mjs" ]