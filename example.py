from melo.api import TTS

# Speed is adjustable
speed = 0.8

# CPU is sufficient for real-time inference.
# You can set it manually to 'cpu' or 'cuda' or 'cuda:0' or 'mps'
device = 'auto' # Will automatically use GPU if available

# English 
text = "Hello this is a test message. ooh!! well it works, i guess."
model = TTS(language='EN_V2', device=device)
print(model)
speaker_ids = model.hps.data.spk2id

# American accent
# output_path = 'en-us.wav'
# model.tts_to_file(text, speaker_ids['EN-US'], output_path, speed=speed)

# British accent
output_path = 'en-br.wav'
model.tts_to_sound(text, speaker_ids['EN-BR'], speed=speed)

# Indian accent
# output_path = 'en-india.wav'
# model.tts_to_file(text, speaker_ids['EN_INDIA'], output_path, speed=speed)

# # Australian accent
# output_path = 'en-au.wav'
# model.tts_to_file(text, speaker_ids['EN-AU'], output_path, speed=speed)

# # Default accent
# output_path = 'en-default.wav'
# model.tts_to_file(text, speaker_ids['EN-Default'], output_path, speed=speed)