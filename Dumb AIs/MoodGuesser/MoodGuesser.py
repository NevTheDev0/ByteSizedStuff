import random
import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense
from keras.activations import relu, softmax

import numpy as np

# Data Collection
data = [
    ("Wow this is so 6 7 awesome!", "Happy"),
    ("FAAAAHHHH", "Angry"),
    ("GRAAHHHHHHH", "Angry"),
    ("I see", "Neutral"),
    ("Who remembers the allomo", "Neutral"),
    ("I wish I were a bird", "Happy"),
    ("Aw, dang it", "Sad"),
    ("Bruh really?", "Sad"),
    ("Really? No WAY", "Happy"),
    ("Uhh ok", "Neutral"),
    ("Haha what is this a mouse band", "Happy"),
    ("NOOOOO not dont do this to me", "Sad"),
    ("I could've done better", "Angry")
]

# Converts the words into 1s and 0s, for the computer to read
vocab = set()
for sentence, _ in data:
    for word in sentence.split():
        vocab.add(word)

vocab_list = sorted(vocab)
vocab_to_index = {word: i for i, word in enumerate(vocab_list)}

features = []
for sentence, _ in data:
    vector = [0] * len(vocab_list)
    for word in sentence.split():
        vector[vocab_to_index[word]] += 1
    features.append(vector)


# Encoding
label_map = {"Happy":0,"Neutral":1,"Sad":2,"Angry":3}
encoded_labels = []
for sentence, sentence_label in data:
    encoded_labels.append(label_map[sentence_label])
combined = []
for i in range(len(features)):
    combined.append((features[i], encoded_labels[i]))

# Shuffling the Data
for i in range(len(combined)):
    j = random.randint(0, (len(combined) - 1))
    temp = combined[i]
    combined[i] = combined[j]
    combined[j] = temp
    print(temp)

n = len(combined)
train_size = int(0.8 * n)

train_set = combined[0: train_size]
test_set = combined[train_size:n]

test_features = []
test_labels = []

for pair in test_set:
    test_features.append(pair[0])
    test_labels.append(pair[1])
train_features = []
train_labels = []

for pair in train_set:
    train_features.append(pair[0])
    train_labels.append(pair[1])

train_x = np.array(train_features)
train_y = np.array(train_labels)

test_x = np.array(test_features)
test_y = np.array(test_labels)


model = Sequential()
model.add(Dense(units= 5,activation='relu',input_shape=(len(vocab_list),)))
model.add(Dense(units=4, activation="softmax"))

model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer=tf.keras.optimizers.Adam(),
    metrics=["accuracy"],
)

model.fit(
    train_x, train_y,
    epochs= 50,
    batch_size=4
)

new_sentence = input("Enter a sentence: ")
vector = [0] * len(vocab_list)
for word in new_sentence.split():
    if word in vocab_to_index:
        vector[vocab_to_index[word]] += 1
new_data = np.array([vector])  # wrap in a batch


accuracy = model.evaluate(test_x, test_y)
predictions = model.predict(new_data)
predicted_class = np.argmax(predictions)

index_to_label = {v: k for k, v in label_map.items()}
predicted_label = index_to_label[predicted_class]
print("Predicted label:", predicted_label)
