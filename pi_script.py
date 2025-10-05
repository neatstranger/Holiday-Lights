import neopixel
import board
import time
import random

pixelCount = 209
pixels = neopixel.NeoPixel(board.D18, pixelCount, auto_write=False)

garage_section = 130
kitchen_section = 209

off = (0, 0, 0)

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
    r = int(r * brightness)
    g = int(g * brightness)
    b = int(b * brightness)

    # Return as BGR instead of RGB
    return (b, g, r)


# ---------- ANIMATIONS ----------

def fade_colors(color1, color2, color3):
    print("Fading color 1...")
    for level in range(0, 10):
        pixels.fill(get_color(color1, brightness=level / 10))
        pixels.show()
        time.sleep(0.02)

    print("Fading color 2...")
    for level in range(0, 10):
        pixels.fill(get_color(color2, brightness=level / 10))
        pixels.show()
        time.sleep(0.02)

    print("Fading color 3...")
    for level in range(0, 10):
        pixels.fill(get_color(color3, brightness=level / 10))
        pixels.show()
        time.sleep(0.02)


def alternating_pattern(color1, color2, color3):
    print("Alternating three colors...")
    for x in range(0, pixelCount, 3):
        pixels[x] = get_color(color1, brightness=0.2)
        if x + 1 < pixelCount:
            pixels[x + 1] = get_color(color2, brightness=0.2)
        if x + 2 < pixelCount:
            pixels[x + 2] = get_color(color3, brightness=0.2)
    pixels.show()


def garage_kitchen_mode_1(color1, color2, color3):
    print("Garage/Kitchen sections – mode 1...")
    for level in range(0, 25):
        for pixel in range(0, garage_section):
            pixels[pixel] = get_color(color1, brightness=level / 25)
        for pixel in range(garage_section, kitchen_section):
            pixels[pixel] = get_color(color2, brightness=level / 25)
        pixels.show()
        time.sleep(0.05)


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
    print("✨ Twinkle sparkle effect...")
    start_time = time.time()
    colors = [get_color(color1), get_color(color2), get_color(color3)]
    while time.time() - start_time < duration:
        # Randomly pick a pixel and color
        idx = random.randint(0, pixelCount - 1)
        pixels[idx] = random.choice(colors)
        pixels.show()
        time.sleep(0.05)
        # Fade it back to off
        pixels[idx] = off
        pixels.show()
        time.sleep(0.05)


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


def breathe_pulse(color1, color2, cycles=3, delay=0.02):
    print("💨 Breathe pulse effect...")
    c1 = get_color(color1)
    c2 = get_color(color2)
    for _ in range(cycles):
        # Fade up
        for b in range(0, 101, 2):
            blend = tuple(int(c1[i] * (1 - b / 100) + c2[i] * (b / 100)) for i in range(3))
            pixels.fill(blend)
            pixels.show()
            time.sleep(delay)
        # Fade down
        for b in range(100, -1, -2):
            blend = tuple(int(c1[i] * (1 - b / 100) + c2[i] * (b / 100)) for i in range(3))
            pixels.fill(blend)
            pixels.show()
            time.sleep(delay)

# ---------- MAIN RUNNERS ----------

def run_sequence(color1, color2, color3):
    fade_colors(color1, color2, color3)
    alternating_pattern(color1, color2, color3)
    garage_kitchen_mode_1(color1, color2, color3)
    garage_kitchen_mode_2(color1, color2, color3)
    twinkle_sparkle(color1, color2, color3)
    chase_wipe(color1, color2, color3)
    breathe_pulse(color1, color2)

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
