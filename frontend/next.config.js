/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ['lablab.ai', 'assemblyai.com'],
  },
  // Allows Vercel compilation setups to route environmental setups easily
  env: {
    NEXT_PUBLIC_ENVIRONMENT: process.env.NODE_ENV,
  },
}

module.exports = nextConfig
