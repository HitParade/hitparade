let mobileMin = 0;
let mobileMax = 767;

let tabletMin = 768;
let tabletMax = 1124;

let desktopMin= 1125;

/**
 * Returns viewport width
 *
 * @returns {Number}
 */
export function getScreenSize () {
  return window.innerWidth;
}

/**
 * Returns bool for screen size
 *
 * @param isScreenSize
 * @returns {boolean}
 */
export function responsive (isScreenSize) {
  let screenSize = getScreenSize();

  if (isScreenSize === 'isMobile') {
    return screenSize >= mobileMin && screenSize <= mobileMax;
  }

  if (isScreenSize === 'isTablet') {
    return screenSize >= tabletMin && screenSize <= tabletMax;
  }

  if (isScreenSize === 'isDesktop') {
    return screenSize >= desktopMin;
  }
}
