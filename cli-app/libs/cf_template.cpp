/*
 *    Author  : Mahad    | github.com/MahadMuhammad
 *    Created : Apr-06-2024   18:24:13   kattis/problems/anewalphabet.cpp
 */

#include <bits/stdc++.h>
using namespace std;

template <typename A, typename B>
ostream &operator<<(ostream &os, const pair<A, B> &p) {
  return os << '(' << p.first << ", " << p.second << ')';
}
template <typename T_container, typename T = typename enable_if<
                                    !is_same<T_container, string>::value,
                                    typename T_container::value_type>::type>
ostream &operator<<(ostream &os, const T_container &v) {
  os << '{';
  string sep;
  for (const T &x : v) os << sep << x, sep = ", ";
  return os << '}';
}

void dbg_out() { cerr << endl; }
template <typename Head, typename... Tail>
void dbg_out(Head H, Tail... T) {
  cerr << ' ' << H;
  dbg_out(T...);
}

#ifdef MAHAD_DEBUG
#define dbg(...) cout << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

unordered_map<char, std::string> char_map{
    {'A', "@"},       {'B', "8"},      {'C', "("},      {'D', "|)"},
    {'E', "3"},       {'F', "#"},      {'G', "6"},      {'H', "[-]"},
    {'I', "|"},       {'J', "_|"},     {'K', "|<"},     {'L', "1"},
    {'M', "[]\\/[]"}, {'N', "[]\\[]"}, {'O', "0"},      {'P', "|D"},
    {'Q', "(,)"},     {'R', "|Z"},     {'S', "$"},      {'T', "']['"},
    {'U', "|_|"},     {'V', "\\/"},    {'W', "\\/\\/"}, {'X', "}{"},
    {'Y', "`/"},      {'Z', "2"}};

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  string s;
  getline(cin, s);
  dbg(s);
  for (char c : s) {
    if ('a' <= c && c <= 'z')
      cout << char_map[c - 32];
    else if ('A' <= c && c <= 'Z')
      cout << char_map[c];
    else
      cout << c;
  }
  return 0;
}