---
title: Scipy — FFT (analyse fréquentielle d'un signal)
type: syntax
columns:
  Nom: col-nom
  Formule / Syntaxe: col-formule
  Params: col-params
  Explication: col-explication
---

## Générer une onde sinusoïdale (signal de test)
Formule / Syntaxe:
```
t = np.**linspace**(0, D, int(R*D))
y = np.**sin**(2*np.pi*f*t)
```
Params:
```
R : taux d'échantillonnage (Hz)
D : durée (s)
f : fréquence (Hz)
```
Explication: une note pure — superposer plusieurs y(t) de fréquences différentes = un accord

## Transformée de Fourier rapide
Formule / Syntaxe:
```
from scipy.fft import **fft, fftfreq**
spectre = fft(y)
freqs = fftfreq(len(y), 1/R)
```
Params: R : même taux d'échantillonnage que pour générer y
Explication: spectre : amplitude complexe par fréquence — fftfreq donne l'axe des fréquences correspondant, à ne garder que sur sa moitié positive (spectre symétrique)

## Écouter un signal (notebook Jupyter)
Formule / Syntaxe:
```
from IPython.display import **Audio**
Audio(y, rate=R)
```
Params: rate : même taux d'échantillonnage R
Explication: lit le tableau numpy comme un fichier audio — pratique pour valider un signal généré/filtré sans l'exporter

## Charger un fichier .wav
Formule / Syntaxe:
```
from scipy.io import wavfile
R, y = wavfile.**read**("son.wav")
```
Params: -
Explication: renvoie le taux d'échantillonnage R et le signal y (array) — même pipeline FFT ensuite que pour un signal généré
