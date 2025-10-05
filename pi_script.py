import neopixel
import board
import time
import random
import math

pixelCount = 209
pixels = neopixel.NeoPixel(board.D18, pixelCount, auto_write=False)

garage_section = 130
kitchen_section = 209

off = (0, 0, 0)
global_brightness = 0.5

# ---------- COLOR HELPER ----------

def get_color(name: str, brightness: float = 1.0) -> tuple:
    """
    Returns a (B, G, R) tuple for the given color name.
    Supports a brightness multiplier (0.0 - 1.0).
    """

    brightness = max(0.0, min(1.0, brightness))

    colors = {
        # --- Christmas ---
        "christmas_red": (255, 0, 0),
        "christmas_green": (0, 255, 0),
        "christmas_gold": (255, 215, 0),

        # --- Halloween ---
        "halloween_orange": (255, 69, 0),
        "halloween_purple": (128, 0, 128),
        "halloween_green": (0, 255, 0),

        # --- Easter ---
        "easter_pink": (255, 182, 193),
        "easter_lavender": (181, 126, 220),
        "easter_yellow": (255, 255, 153),

        # --- Valentine’s ---
        "valentine_red": (255, 0, 64),
        "valentine_pink": (255, 105, 180),
        "valentine_white": (255, 255, 255),

        # --- 4th of July ---
        "independence_red": (255, 0, 0),
        "independence_white": (255, 255, 255),
        "independence_blue": (0, 0, 255),

        # --- St. Patrick’s ---
        "patrick_green": (0, 128, 0),
        "patrick_gold": (255, 215, 0),
        "patrick_white": (255, 255, 255),

        # --- Generic ---
        "white": (255, 255, 255),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "orange": (255, 165, 0),
        "purple": (128, 0, 128),
        "teal": (0, 128, 128),
        "pink": (255, 105, 180),
        "warm_white": (255, 180, 100)
    }

    r, g, b = colors.get(name.lower(), (255, 255, 255))
    r = int(r * brightness * global_brightness)
    g = int(g * brightness * global_brightness)
    b = int(b * brightness * global_brightness)

    # Return as BGR instead of RGB
    return (b, g, r)


# ---------- ANIMATIONS ----------

def ease_brightness(step, total_steps):
    """Smooth fade-in/out curve using a sine easing."""
    return math.sin((step / total_steps) * (math.pi / 2))



def fade_colors(color1, color2, color3, steps=50, delay=0.03):
    print("🌈 Smooth fade through three colors...")
    sequence = [color1, color2, color3]
    
    for i in range(len(sequence)):
        c_start = get_color(sequence[i])
        c_end = get_color(sequence[(i + 1) % len(sequence)])
        
        for step in range(steps + 1):
            t = ease_brightness(step, steps)
            blend = tuple(int(c_start[j] * (1 - t) + c_end[j] * t) for j in range(3))
            pixels.fill(blend)
            pixels.show()
            time.sleep(delay)


def alternating_pattern(color1, color2, color3):
    print("Alternating three colors...")
    for x in range(0, pixelCount, 3):
        pixels[x] = get_color(color1, brightness=0.2)
        if x + 1 < pixelCount:
            pixels[x + 1] = get_color(color2, brightness=0.2)
        if x + 2 < pixelCount:
            pixels[x + 2] = get_color(color3, brightness=0.2)
    pixels.show()


def garage_kitchen_mode_1(color1, color2, color3, steps=40, delay=0.03):
    print("Garage/Kitchen sections – smooth fade mode 1...")
    for step in range(steps + 1):
        b = ease_brightness(step, steps)
        for pixel in range(0, garage_section):
            pixels[pixel] = get_color(color1, brightness=b)
        for pixel in range(garage_section, kitchen_section):
            pixels[pixel] = get_color(color2, brightness=b)
        pixels.show()
        time.sleep(delay)


def garage_kitchen_mode_2(color1, color2, color3):
    print("Garage/Kitchen sections – mode 2...")
    for level in range(0, 25):
        for pixel in range(0, garage_section):
            pixels[pixel] = get_color(color2, brightness=level / 25)
        for pixel in range(garage_section, kitchen_section):
            pixels[pixel] = get_color(color3, brightness=level / 25)
        pixels.show()
        time.sleep(0.05)

def twinkle_sparkle(color1, color2, color3, duration=10):
    print("✨ Twinkle sparkle with fades...")
    start_time = time.time()
    colors = [get_color(color1), get_color(color2), get_color(color3)]

    while time.time() - start_time < duration:
        idx = random.randint(0, pixelCount - 1)
        c = random.choice(colors)

        # fade in
        for step in range(0, 20):
            b = ease_brightness(step, 20)
            pixels[idx] = tuple(int(ch * b) for ch in c)
            pixels.show()
            time.sleep(0.01)

        # fade out
        for step in range(20, -1, -1):
            b = ease_brightness(step, 20)
            pixels[idx] = tuple(int(ch * b) for ch in c)
            pixels.show()
            time.sleep(0.01)


def chase_wipe(color1, color2, color3, delay=0.01):
    print("🏃 Chase wipe effect...")
    colors = [get_color(color1), get_color(color2), get_color(color3)]
    for i in range(pixelCount + 20):  # go slightly beyond for smooth exit
        for j in range(pixelCount):
            color_idx = (i - j) % len(colors)
            if i - j >= 0:
                pixels[j] = colors[color_idx]
        pixels.show()
        time.sleep(delay)


def breathe_pulse(color1, color2, cycles=None, delay=0.02):
    print("💨 Breathe pulse effect (more organic)...")
    if cycles is None:
        cycles = random.randint(2, 5)

    c1 = get_color(color1)
    c2 = get_color(color2)

    for _ in range(cycles):
        for b in range(0, 101, 2):
            blend = tuple(int(c1[i] * (1 - b / 100) + c2[i] * (b / 100)) for i in range(3))
            pixels.fill(blend)
            pixels.show()
            time.sleep(delay + random.uniform(-0.005, 0.01))  # slight jitter
        for b in range(100, -1, -2):
            blend = tuple(int(c1[i] * (1 - b / 100) + c2[i] * (b / 100)) for i in range(3))
            pixels.fill(blend)
            pixels.show()
            time.sleep(delay + random.uniform(-0.005, 0.01))


def meteor_rain(color1, color2, color3, meteor_size=10, meteor_trail_decay=0.8, delay=0.03):
    print("☄️ Meteor rain effect...")
    colors = [get_color(color1), get_color(color2), get_color(color3)]
    pixels.fill(off)

    for i in range(pixelCount * 2):
        # fade all pixels a bit
        for j in range(pixelCount):
            r, g, b = pixels[j]
            pixels[j] = (int(r * meteor_trail_decay), int(g * meteor_trail_decay), int(b * meteor_trail_decay))

        # draw the meteor
        for j in range(meteor_size):
            if 0 <= i - j < pixelCount:
                pixels[i - j] = random.choice(colors)

        pixels.show()
        time.sleep(delay)

def color_wave(color1, color2, color3, speed=0.05):
    print("🌊 Color wave effect...")
    base_colors = [get_color(color1), get_color(color2), get_color(color3)]
    steps = 256

    for step in range(steps):
        for i in range(pixelCount):
            # phase shift each pixel by its position
            phase = (i * 256 // pixelCount + step) % 256
            c1 = base_colors[0]
            c2 = base_colors[1]
            c3 = base_colors[2]
            if phase < 85:
                color = (
                    int(c1[0] * (255 - phase * 3) / 255 + c2[0] * (phase * 3) / 255),
                    int(c1[1] * (255 - phase * 3) / 255 + c2[1] * (phase * 3) / 255),
                    int(c1[2] * (255 - phase * 3) / 255 + c2[2] * (phase * 3) / 255)
                )
            elif phase < 170:
                phase -= 85
                color = (
                    int(c2[0] * (255 - phase * 3) / 255 + c3[0] * (phase * 3) / 255),
                    int(c2[1] * (255 - phase * 3) / 255 + c3[1] * (phase * 3) / 255),
                    int(c2[2] * (255 - phase * 3) / 255 + c3[2] * (phase * 3) / 255)
                )
            else:
                phase -= 170
                color = (
                    int(c3[0] * (255 - phase * 3) / 255 + c1[0] * (phase * 3) / 255),
                    int(c3[1] * (255 - phase * 3) / 255 + c1[1] * (phase * 3) / 255),
                    int(c3[2] * (255 - phase * 3) / 255 + c1[2] * (phase * 3) / 255)
                )
            pixels[i] = color
        pixels.show()
        time.sleep(speed)

def bar_sweep(color1, color2, color3, bar_width=5, delay=0.01):
    print("📶 Bar sweep animation...")

    # Step 1 – fill with base color
    pixels.fill(get_color(color1))
    pixels.show()
    time.sleep(0.3)

    # Step 2 – bar moves left ➡ right
    c2 = get_color(color2)
    for pos in range(-bar_width, pixelCount + bar_width):
        pixels.fill(get_color(color1))  # reset to base color
        for i in range(pos, pos + bar_width):
            if 0 <= i < pixelCount:
                pixels[i] = c2
        pixels.show()
        time.sleep(delay)

    time.sleep(0.3)  # brief pause

    # Step 3 – bar moves right ➡ left
    c3 = get_color(color3)
    for pos in range(pixelCount + bar_width, -bar_width, -1):
        pixels.fill(get_color(color1))
        for i in range(pos - bar_width, pos):
            if 0 <= i < pixelCount:
                pixels[i] = c3
        pixels.show()
        time.sleep(delay)


def fade_to_black(steps=30, delay=0.02):
    for step in range(steps, -1, -1):
        b = ease_brightness(step, steps)
        for i in range(pixelCount):
            r, g, bl = pixels[i]
            pixels[i] = (int(bl * b), int(g * b), int(r * b))
        pixels.show()
        time.sleep(delay)


# ---------- MAIN RUNNERS ----------

def run_sequence(color1, color2, color3):
    animations = [
        lambda: fade_colors(color1, color2, color3),
        lambda: alternating_pattern(color1, color2, color3),
        lambda: garage_kitchen_mode_1(color1, color2, color3),
        lambda: garage_kitchen_mode_2(color1, color2, color3),
        lambda: twinkle_sparkle(color1, color2, color3),
        lambda: chase_wipe(color1, color2, color3),
        lambda: breathe_pulse(color1, color2),
        lambda: meteor_rain(color1, color2, color3),
        lambda: color_wave(color1, color2, color3),
        lambda: bar_sweep(color1, color2, color3),
    ]

    # Randomize the order and length of the sequence
    chosen_animations = random.sample(animations, random.randint(4, len(animations)))

    for anim in chosen_animations:
        # optional fade-in: start from black to avoid jarring start
        fade_to_black(steps=10, delay=0.01)

        anim()  # run the actual animation
        
        # fade out gracefully before moving on
        fade_to_black(steps=30, delay=0.02)

        # tiny pause to make transitions feel intentional
        time.sleep(0.2)

        

def run_holiday(holiday: str):
    """
    Runs the animation sequence for a given holiday.
    """

    holiday = holiday.lower()
    palettes = {
        "christmas": ("christmas_red", "christmas_green", "christmas_gold"),
        "halloween": ("halloween_orange", "halloween_purple", "halloween_green"),
        "easter": ("easter_pink", "easter_lavender", "easter_yellow"),
        "valentine": ("valentine_red", "valentine_pink", "valentine_white"),
        "4thofjuly": ("independence_red", "independence_white", "independence_blue"),
        "independence": ("independence_red", "independence_white", "independence_blue"),
        "patrick": ("patrick_green", "patrick_gold", "patrick_white"),
        "stpatricks": ("patrick_green", "patrick_gold", "patrick_white")
    }

    if holiday not in palettes:
        print(f"⚠️ Unknown holiday '{holiday}', defaulting to white/green/red.")
        palettes[holiday] = ("white", "green", "red")

    c1, c2, c3 = palettes[holiday]
    print(f"🎉 Running sequence for {holiday.capitalize()} with colors: {c1}, {c2}, {c3}")
    run_sequence(c1, c2, c3)


# ---------- SCRIPT START ----------

if __name__ == "__main__":
    pixels.fill(off)
    pixels.show()
    try:
        while True:
            run_holiday("halloween")   # 🎄 Just change this word to swap themes!
            # run_holiday("halloween")
            # run_holiday("patrick")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping and clearing LEDs...")
        pixels.fill(off)
        pixels.show()
