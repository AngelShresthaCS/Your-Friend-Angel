export default async function ChatInterfacePage() {
  const messages = [
    {
      id: 1,
      role: 'user',
      name: 'You',
      text: 'Hii9',
      time: 'Just now',
    },
    {
      id: 2,
      role: 'assistant',
      name: 'Angel Bot',
      text: 'hello',
      time: 'Just now',
    },
  ]
  let chatmessage = null;
  try {
        const message = await fetch(`http://127.0.0.1:8000/message`, {
            cache: "no-store",
        });
        chatmessage = await message.json();
        console.log(chatmessage);
    } catch {
      chatmessage = null;
    }
  return (
    <main
      className="min-h-screen p-6 text-slate-900"
      style={{
        background:
          'radial-gradient(circle at top, rgba(255, 214, 170, 0.5), transparent 38%), linear-gradient(180deg, #fffaf3 0%, #f2ece4 100%)',
      }}
    >
      <div className="min-h-[calc(100vh-48px)] max-w-[1120px] mx-auto overflow-hidden border border-white/72 rounded-2xl bg-white/80 backdrop-blur-[18px] shadow-[0_24px_80px_rgba(15,23,42,0.12)]">
        <header className="flex flex-col gap-4 p-6 border-b border-slate-200/75">
          <div />
        </header>

        <section className="grid min-h-0 grid-cols-[minmax(0,1.35fr)_minmax(280px,0.85fr)] md:grid-cols-1">
          <div className="flex min-h-0 flex-col border-r border-slate-200/75 bg-white/75">
            <div className="flex items-center justify-between gap-3 p-4 border-b border-slate-200/75">
              <div>
                <p className="m-0 text-slate-500 text-sm font-medium">Conversation</p>
              </div>
            </div>

            <div className="flex flex-1 flex-col gap-4 overflow-y-auto p-6">
              {messages.map((message) => (
                <article
                  key={message.id}
                  className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
                >
                  <div
                    className={`max-w-[85%] p-4 rounded-[24px] shadow-[0_10px_24px_rgba(15,23,42,0.08)] ${
                      message.role === 'user'
                        ? 'rounded-br-[10px] text-white bg-gradient-to-br from-slate-900 to-slate-800'
                        : 'border border-slate-200/95 rounded-bl-[10px] text-slate-900 bg-white/98'
                    }`}
                  >
                    <div className="flex items-center gap-2 text-[0.72rem] font-semibold opacity-80">
                      <span>{message.name} </span>
                      <span aria-hidden="true">•</span>
                      <span>{message.time}</span>
                    </div>
                    <p className="mt-2 text-sm leading-6">{chatmessage ? `(${chatmessage.message})` : ""}</p>
                  </div>
                </article>
              ))}

            </div>
            

            <form className="p-4 border-t border-slate-200/75 bg-white/80">
              <div className="flex flex-col sm:flex-row gap-3 sm:items-end p-3 border border-slate-200 rounded-2xl bg-slate-50 shadow-inner">
                <label className="sr-only" htmlFor="message">
                  Type a message
                </label>
                <textarea
                  id="message"
                  name="message"
                  rows={1}
                  placeholder="Type a message..."
                  className="min-h-[48px] flex-1 resize-none border-transparent rounded-lg px-4 py-3 text-slate-900 bg-white outline-none focus:border-amber-300 focus:ring-4 focus:ring-amber-200/30"
                />
                <button
                  type="button"
                  className="w-full sm:w-auto rounded-lg px-5 py-3 text-white bg-gradient-to-br from-slate-900 to-slate-800 text-sm font-bold hover:-translate-y-0.5 hover:shadow-lg transition-transform"
                >
                  Send
                </button>
                
              </div>
            </form>
          </div>
        </section>
      </div>
    </main>
  )
}
