import enum

class Feeling(enum.Enum):
    Sad = 1
    Neutral = 2
    Happy = 3

feelingColorMap = {
    Feeling.Sad: ["#394e7a", "#8e9ac7", "#4ee"],
    Feeling.Neutral: ["#22d", "#c8f8ff", "#6d2"],
    Feeling.Happy: ["#39f", "#f4e54d", "#fa3"],
}

feelingLabelMap = {
    Feeling.Sad: "Could be better",
    Feeling.Neutral: "Okay",
    Feeling.Happy: "Happy",
}

class App:
    def __init__(self):
        self.wrapperRef = None
        self.feeling = Feeling.Neutral
        self.render()

    def set_feeling(self, value: int):
        self.feeling = Feeling(value)
        self.update_styles()

    def update_styles(self):
        if not self.wrapperRef:
            return

        a, b, c = feelingColorMap[self.feeling]
        self.wrapperRef['style'] = f"""
            --color-a: {a};
            --color-b: {b};
            --color-c: {c};
        """

    def render(self):
        feeling_label = feelingLabelMap[self.feeling]
        html_content = f"""
        <main class="flex min-h-[100dvh] w-full items-center justify-center">
            <div
                ref="wrapperRef"
                class="relative mx-auto aspect-[9/16] w-[360px] max-w-full overflow-hidden rounded-2xl bg-gradient-to-br from-[--color-a] via-[--color-b] to-[--color-c] p-8 text-white duration-500 ease-in-out animate-gradient [transition-property:_--color-a,_--color-b,_--color-c]"
            >
                <div class="relative z-10">
                    <h1 class="mb-12 text-5xl font-medium leading-tight">
                        How are you feeling today?
                    </h1>
                    <h2 class="mb-4 text-center text-2xl font-medium">
                        {feeling_label}
                    </h2>
                    <input
                        class="range"
                        onChange="lambda ev: self.set_feeling(int(ev.target.value))"
                        type="range"
                        min="1"
                        value="{self.feeling.value}"
                        max="3"
                        step="1"
                    />
                </div>
            </div>
        </main>
        <style>
        @keyframes gradient {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        .animate-gradient {
            background: linear-gradient(-45deg, var(--color-a), var(--color-b), var(--color-c));
            background-size: 300% 300%;
            animation: gradient 15s ease infinite;
        }
        </style>
        """
        self.wrapperRef = {"style": ""}
        self.update_styles()
        return html_content

app = App()
html_content = app.render()

# Save the HTML content to a file
with open("index.html", "w") as file:
    file.write(html_content)

print("HTML content saved to index.html")
