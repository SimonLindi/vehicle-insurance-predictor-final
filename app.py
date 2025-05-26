import gradio as gr
import joblib
import numpy as np

# Modell laden
model = joblib.load("random_forest_hf_compatible.pkl")

# Vorhersagefunktion
def predict_premium(vehicle_age, price_clean, avg_yearly_value, horsepower, power_to_weight):
    # Input als numpy-Array im richtigen Format
    X = np.array([[vehicle_age, price_clean, avg_yearly_value, horsepower, power_to_weight]])
    prediction = model.predict(X)[0]
    return f"{prediction:.2f} CHF"

# Gradio-UI
demo = gr.Interface(
    fn=predict_premium,
    inputs=[
        gr.Number(label="Fahrzeugalter bei Versicherungsbeginn (Jahre)"),
        gr.Number(label="Aktueller Fahrzeugwert (CHF)"),
        gr.Number(label="Ø Wertverlust pro Jahr (CHF)"),
        gr.Number(label="PS (Horsepower)"),
        gr.Number(label="PS pro Tonne (power-to-weight)"),  # 👈 NEU
    ],
    outputs=gr.Text(label="Geschätzte Versicherungsprämie (CHF)"),
    title="Versicherungsprämien-Vorhersage",
    description="Basierend auf Fahrzeugmerkmalen und Wertentwicklung"
)

if __name__ == "__main__":
    demo.launch()