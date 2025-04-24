{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f08cc7c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.\n",
      "2025-04-22 11:08:01.449 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 11:08:01.993 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\LENOVO\\AppData\\Roaming\\Python\\Python310\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-04-22 11:08:01.994 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 11:08:01.996 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 11:08:01.996 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 11:08:01.997 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 11:08:01.997 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 11:08:01.998 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 11:08:01.998 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 11:08:01.998 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 11:08:01.999 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-22 11:08:01.999 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "from tensorflow.keras.models import load_model\n",
    "from tensorflow.keras.preprocessing import image\n",
    "from PIL import Image\n",
    "\n",
    "model = load_model('gesture_model.h5')\n",
    "class_names = ['A', 'B', 'C', 'D', 'E']  # Replace with your actual classes\n",
    "\n",
    "st.title(\"Hand Gesture Recognition\")\n",
    "st.write(\"Upload an image to classify the hand gesture\")\n",
    "\n",
    "uploaded_file = st.file_uploader(\"Choose an image...\", type=[\"jpg\", \"png\", \"jpeg\"])\n",
    "if uploaded_file is not None:\n",
    "    img = Image.open(uploaded_file).resize((64, 64))\n",
    "    st.image(img, caption=\"Uploaded Image\", use_column_width=True)\n",
    "\n",
    "    x = image.img_to_array(img)\n",
    "    x = np.expand_dims(x, axis=0) / 255.0\n",
    "\n",
    "    preds = model.predict(x)\n",
    "    predicted = class_names[np.argmax(preds)]\n",
    "\n",
    "    st.success(f\"Prediction: {predicted}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
