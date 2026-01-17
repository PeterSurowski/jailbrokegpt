import { useState } from 'react'
import ChatInterface from './components/ChatInterface'

function App() {
  return (
    <div className="min-h-screen bg-gray-900">
      <header className="bg-gray-800 border-b border-gray-700 py-4 px-6">
        <div className="max-w-4xl mx-auto flex items-center justify-between">
          <h1 className="text-2xl font-bold text-white">
            JailbrokeGPT
          </h1>
          <span className="text-sm text-gray-400">
            Uncensored AI Chat
          </span>
        </div>
      </header>
      
      <main className="max-w-4xl mx-auto p-4">
        <ChatInterface />
      </main>
      
      <footer className="fixed bottom-0 left-0 right-0 bg-gray-800 border-t border-gray-700 py-2 px-6 text-center">
        <p className="text-xs text-gray-500">
          Built by Peter Surowski | Copyright 2026
        </p>
      </footer>
    </div>
  )
}

export default App
