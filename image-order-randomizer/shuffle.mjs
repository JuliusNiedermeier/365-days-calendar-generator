export function shuffleArray(originalArray) {
  // Create a copy of the original array
  const array = [...originalArray];

  // Shuffle the copy using the Fisher-Yates algorithm
  for (let i = array.length - 1; i > 0; i--) {
    // Generate a random index
    const j = Math.floor(Math.random() * (i + 1));

    // Swap elements at indices i and j in the copy
    [array[i], array[j]] = [array[j], array[i]];
  }

  // Return the shuffled copy
  return array;
}
