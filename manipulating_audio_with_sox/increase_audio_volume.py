import pysox
infile = pysox.CSoxStream('test.wav')
outfile = pysox.CSoxStream('out.wav','w',infile.get_signal())

# Then we define an effectschain which will do all the work.
chain = pysox.CEffectsChain(infile, outfile)

# An effect is added to the chain, see the sox manpage for available effects.
# The example below will increase the volume by 18 decibels
effect = pysox.CEffect("vol", [ b'18dB' ])
chain.add_effect(effect)

# All is set up, now we flow the audio through the chain
chain.flow_effects()
outfile.close()
