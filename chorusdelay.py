
src = Input([0,1])



# DSP

a = Delay(src, delay=.6, feedback=.05, mul=.05).out(0)
b = Delay(src, delay=.8, feedback=.05, mul=.05).out(1)
c = Delay(src, delay=.5, feedback=.05, mul=.05).out()


# Sets values for 8 LFO'ed delay lines (you can add more if you want!).
# LFO frequencies.
freqs = [0.35, 0.4, 0.42, 0.37]
# Center delays in seconds.
cdelay = [0.0236, 0.030, 0.036, 0.047]
# Modulation depths in seconds.
adelay = [0.003, 0.003, 0.003, 0.003]

# Create 8 sinusoidal LFOs with center delays "cdelay" and depths "adelay".
lfos = Sine(freqs, mul=adelay, add=cdelay)

# Create 4 modulated delay lines with a little feedback and send the signals
# to the output. Streams 1, 3, 5, 7 to the left and streams 2, 4, 6, 8 to the
# right (default behaviour of the out() method).
delays = Delay(src, lfos, feedback=0.0001, mul=0.37).out()


dry = Mix(src, voices=2, mul=0.7).out()
