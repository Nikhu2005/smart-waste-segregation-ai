import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load model
model = load_model("model.h5")

# Your class names (copy exactly from output)
classes = [
'(BT) Body Tissue or Organ',
'(GE) Glass equipment-packaging 551',
'(ME) Metal equipment -packaging',
'(OW) Organic wastes',
'(PE) Plastic equipment-packaging',
'(PP) Paper equipment-packaging',
'(SN) Syringe needles',
'Gauze',
'Gloves',
'Mask',
'Syringe',
'Tweezers'
]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = cv2.resize(frame, (224,224))
    img = np.expand_dims(img, axis=0) / 255.0

    prediction = model.predict(img)
    label = classes[np.argmax(prediction)]

    cv2.putText(frame, label, (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.imshow("Bio Waste Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()