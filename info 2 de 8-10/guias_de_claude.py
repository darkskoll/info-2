# Una clase es el plano de una casa. Un objeto es la casa construida a partir de ese plano.
class Perro:
    def __init__(self, nombre):  # constructor: se ejecuta al crear el objeto
        self.nombre = nombre     # atributo

    def ladrar(self):            # método
        print(f"{self.nombre} dice: ¡Guau!")

mi_perro = Perro("Rex")   # objeto
mi_perro.ladrar()         # → Rex dice: ¡Guau!

#2. Encapsulación
#Proteger los datos internos de una clase para que no se modifiquen accidentalmente.

class Señal:
    def __init__(self, fs):
        self.__fs = fs  # __ = privado, nadie lo toca desde afuera directamente

    def get_fs(self):   # solo se accede así (getter)
        return self.__fs
    
# _atributo → protegido (convención: "úsalo con cuidado")
# __atributo → privado (Python lo oculta de verdad)

# 3. Herencia
# Una clase "hija" hereda todo de una clase "madre" y puede agregar o cambiar cosas.
class Animal:
    def hablar(self):
        pass  # método base, vacío

class Perro(Animal):      # Perro hereda de Animal
    def hablar(self):
        print("Guau")

class Gato(Animal):       # Gato hereda de Animal
    def hablar(self):
        print("Miau")




### 4. Polimorfismo

# El **mismo método** (`hablar`) se comporta diferente según la clase. En tu proyecto, el método `process()` hará cosas distintas para ECG y para EMG, pero se llama igual.



### 5. Señales: ¿artificiales o dataset?
"""
**Te recomiendo señales artificiales** por estas razones:
- No necesitas descargar nada
- Tú controlas el ruido, la duración, la frecuencia
- Es más fácil de explicar y defender en clase
- Igualmente se ven realistas si se generan bien

Vamos a simular una señal ECG con picos tipo QRS y una señal EMG con ráfagas de activación muscular, ambas con ruido gaussiano añadido.

---

## 🗂️ Estructura del proyecto

Antes de escribir código, mira cómo lo vamos a organizar:
```
proyecto/
│
├── signal_base.py       ← Clase base: Signal
├── processor.py         ← Clase base: Processor + subclases ECGProcessor, EMGProcessor
├── ecg_signal.py        ← Clase ECGSignal (hereda de Signal)
├── emg_signal.py        ← Clase EMGSignal (hereda de Signal)
└── main.py              ← Script principal que une todo

"""