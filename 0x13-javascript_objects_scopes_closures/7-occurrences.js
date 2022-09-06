#!/usr/bin/node

/**
 * computes the number of occurrence of an element
 * @param {Array} list The list of elements.
 * @param {Any} searchElement The element to look for.
 * @returns {Number} The number of occurrences of the given element.
 */
exports.nbOccurences = function (list, searchElement) {
  return list.filter( item => item === searchElement).length;
};
