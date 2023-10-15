export const popVisibleOnceMotion = {
  initial: { opacity: 0, scale: 0.8 },
  visibleOnce: { opacity: 1, scale: 1, transition: { duration: 300 } },
  delay: 200
}

export const slideVisibleOnceMotion = {
  initial: { opacity: 0 },
  visibleOnce: { opacity: 1, transition: { duration: 1500 } },
  delay: 800
}

export const slideVisibleOnceBottomMotion = {
  initial: { opacity: 0, y: 50 },
  visibleOnce: { opacity: 1, y: 0, transition: { duration: 800 } },
  delay: 500
}

export const slideVisibleOnceLeftMotion = {
  initial: { opacity: 0, x: -50 },
  visibleOnce: { opacity: 1, x: 0, transition: { duration: 800 } },
  delay: 500
}

export const slideVisibleOnceRightMotion = {
  initial: { opacity: 0, x: 50 },
  visibleOnce: { opacity: 1, x: 0, transition: { duration: 800 } },
  delay: 500
}
