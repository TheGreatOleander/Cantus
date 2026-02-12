import librosa
import numpy as np

NOTE_TO_OP = {
    0: "PUSH", 1: "DUP", 2: "ADD", 3: "SWAP", 4: "SUB", 
    5: "MUL", 6: "DROP", 7: "DIV", 8: "OVER", 9: "JUMP", 
    10: "ROT", 11: "IF_ZERO"
}

def tokenize(audio_path):
    if not audio_path:
        return [("PUSH", 10), ("DUP", 0), ("MUL", 0)] # Default: returns 100

    y, sr = librosa.load(audio_path)
    
    # Use pYIN for high-accuracy pitch tracking
    f0, voiced_flag, voiced_probs = librosa.pyin(
        y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7')
    )
    
    tokens = []
    last_midi = None
    stable_count = 0
    DEBOUNCE = 3  # Note must be stable for 3 frames to count as an instruction

    for freq in f0:
        if not np.isnan(freq):
            midi_note = int(round(librosa.hz_to_midi(freq)))
            
            if midi_note == last_midi:
                stable_count += 1
            else:
                if stable_count >= DEBOUNCE:
                    note_idx = last_midi % 12
                    octave = last_midi // 12
                    tokens.append((NOTE_TO_OP.get(note_idx), octave))
                
                last_midi = midi_note
                stable_count = 1
                
    return tokens