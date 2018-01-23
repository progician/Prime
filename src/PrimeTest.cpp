#include "Prime/PrimeTest.h"
#include <cmath>

bool IsPrime( int n ) {
  for ( int i = 2; i < std::sqrt( n ); i++ ) {
    if ( n % i == 0 )
      return false;
  }
  return true;
}
