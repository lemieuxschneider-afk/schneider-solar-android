__version__ = "1.0.0"

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.clearcolor = (0.055, 0.12, 0.16, 1)

class SolarApp(App):
    def build(self):
        self.title = "SCHNEIDER SOLAR"
        root = BoxLayout(orientation="vertical", padding=dp(12), spacing=dp(8))

        header = Label(
            text="[b]SCHNEIDER SOLAR[/b]\\nDimensionnement photovoltaïque hors ligne",
            markup=True, size_hint_y=None, height=dp(70),
            color=(1, 0.78, 0.25, 1), font_size="20sp",
            halign="center", valign="middle"
        )
        root.add_widget(header)

        scroll = ScrollView()
        content = BoxLayout(orientation="vertical", spacing=dp(8),
                            size_hint_y=None, padding=(0, dp(4)))
        content.bind(minimum_height=content.setter("height"))

        self.fields = {}
        defaults = [
            ("Consommation quotidienne (kWh)", "5.025", "conso"),
            ("Heures de soleil équivalentes (HSP)", "3.5", "hsp"),
            ("Rendement global solaire (%)", "75", "rendement"),
            ("Puissance d'un panneau (W)", "500", "panneau"),
            ("Tension batterie nominale (V)", "25.6", "voltage"),
            ("Profondeur de décharge batterie (%)", "80", "dod"),
            ("Rendement onduleur (%)", "90", "eff"),
            ("Autonomie souhaitée (jours)", "1", "jours"),
            ("Puissance simultanée des appareils (W)", "505", "charge"),
        ]
        for label_text, value, key in defaults:
            label = Label(text=label_text, size_hint_y=None, height=dp(28),
                          halign="left", valign="middle", color=(0.93,0.96,0.97,1))
            label.bind(size=lambda inst, val: setattr(inst, "text_size", val))
            content.add_widget(label)
            inp = TextInput(text=value, multiline=False, input_filter="float",
                            size_hint_y=None, height=dp(44), font_size="17sp",
                            background_color=(0.12,0.21,0.25,1),
                            foreground_color=(1,1,1,1), cursor_color=(1,0.78,0.25,1))
            self.fields[key] = inp
            content.add_widget(inp)

        calc = Button(text="CALCULER LE DIMENSIONNEMENT", size_hint_y=None,
                      height=dp(52), background_normal="",
                      background_color=(0.88,0.63,0.12,1),
                      color=(0.05,0.10,0.12,1), bold=True)
        calc.bind(on_release=self.calculate)
        content.add_widget(calc)

        self.output = Label(text="Entre tes paramètres puis appuie sur CALCULER.",
                            markup=True, size_hint_y=None, height=dp(300),
                            halign="left", valign="top", color=(1,1,1,1),
                            font_size="15sp")
        self.output.bind(size=lambda inst, val: setattr(inst, "text_size", (val[0], None)))
        self.output.bind(texture_size=lambda inst, val: setattr(inst, "height", max(dp(300), val[1] + dp(20))))
        content.add_widget(self.output)

        warning = Label(
            text="IMPORTANT : résultats préliminaires. Vérifie les fiches techniques, "
                 "la tension Voc à froid, les limites du MPPT, les courants de démarrage, "
                 "les câbles, fusibles, disjoncteurs et la mise à la terre avec un professionnel.",
            size_hint_y=None, height=dp(110), color=(1,0.72,0.45,1),
            font_size="12sp", halign="left", valign="middle"
        )
        warning.bind(size=lambda inst, val: setattr(inst, "text_size", val))
        content.add_widget(warning)
        scroll.add_widget(content)
        root.add_widget(scroll)
        return root

    def val(self, key, fallback):
        try:
            x = float(self.fields[key].text.strip())
            return x if x > 0 else fallback
        except Exception:
            return fallback

    def calculate(self, *_):
        conso = self.val("conso", 5.025)
        hsp = self.val("hsp", 3.5)
        rendement = min(100, self.val("rendement", 75)) / 100
        panneau = self.val("panneau", 500)
        voltage = self.val("voltage", 25.6)
        dod = min(100, self.val("dod", 80)) / 100
        eff = min(100, self.val("eff", 90)) / 100
        jours = self.val("jours", 1)
        charge = self.val("charge", 505)

        pv_min_w = conso * 1000 / (hsp * rendement)
        pv_target_w = pv_min_w * 1.20
        n_pan = int(-(-pv_target_w // panneau))
        pv_installe = n_pan * panneau
        production = pv_installe / 1000 * hsp * rendement
        batterie_kwh = conso * jours / (dod * eff) * 1.15
        batterie_ah = batterie_kwh * 1000 / voltage
        mppt_a = pv_installe / voltage / 0.95 * 1.25
        onduleur_w = max(1000, charge * 1.5)

        self.output.text = (
            "[b]RÉSULTATS ESTIMÉS[/b]\\n\\n"
            f"Puissance PV théorique : {pv_min_w/1000:.2f} kWc\\n"
            f"Cible avec marge de 20 % : {pv_target_w/1000:.2f} kWc\\n"
            f"Panneaux nécessaires : {n_pan} × {panneau:.0f} W\\n"
            f"Puissance PV installée : {pv_installe/1000:.2f} kWc\\n"
            f"Production estimée : {production:.2f} kWh/jour\\n\\n"
            f"Batterie nominale visée : {batterie_kwh:.2f} kWh\\n"
            f"Capacité indicative : {batterie_ah:.0f} Ah à {voltage:.1f} V\\n"
            f"Onduleur estimatif : au moins {onduleur_w:.0f} W continus\\n"
            f"Courant MPPT indicatif : environ {mppt_a:.0f} A\\n\\n"
            "[b]À vérifier avant achat[/b]\\n"
            "• La tension et le courant d'entrée PV admissibles du MPPT.\\n"
            "• Les valeurs Voc/Vmp/Isc/Imp des panneaux et leur câblage série/parallèle.\\n"
            "• Le courant de démarrage du réfrigérateur et la puissance de crête de l'onduleur.\\n"
            "• Les protections DC/AC, sections de câbles et la mise à la terre."
        )

if __name__ == "__main__":
    SolarApp().run()
