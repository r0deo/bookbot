file_path = './books/frankenstein.txt'

# Open and read the file
with open(file_path, "r") as file:
    content = file.read().lower()  # Convert text to lowercase to handle case insensitivity

# Initialize counters for each character as integers (not strings)
count_a = count_b = count_c = count_d = count_e = count_f = count_g = count_h = 0
count_i = count_j = count_k = count_l = count_m = count_n = count_o = count_p = 0
count_q = count_r = count_s = count_t = count_u = count_v = count_w = count_x = 0
count_y = count_z = 0

# Loop through the content and count the occurrences of each character
for c in content:
    if c == 'a':
        count_a += 1
    elif c == 'b':
        count_b += 1
    elif c == 'c':
        count_c += 1
    elif c == 'd':
        count_d += 1
    elif c == 'e':
        count_e += 1
    elif c == 'f':
        count_f += 1
    elif c == 'g':
        count_g += 1
    elif c == 'h':
        count_h += 1
    elif c == 'i':
        count_i += 1
    elif c == 'j':
        count_j += 1
    elif c == 'k':
        count_k += 1
    elif c == 'l':
        count_l += 1
    elif c == 'm':
        count_m += 1
    elif c == 'n':
        count_n += 1
    elif c == 'o':
        count_o += 1
    elif c == 'p':
        count_p += 1
    elif c == 'q':
        count_q += 1
    elif c == 'r':
        count_r += 1
    elif c == 's':
        count_s += 1
    elif c == 't':
        count_t += 1
    elif c == 'u':
        count_u += 1
    elif c == 'v':
        count_v += 1
    elif c == 'w':
        count_w += 1
    elif c == 'x':
        count_x += 1
    elif c == 'y':
        count_y += 1
    elif c == 'z':
        count_z += 1

# Print the results
print(f"The 'a' character was found {count_a} times")
print(f"The 'b' character was found {count_b} times")
print(f"The 'c' character was found {count_c} times")
print(f"The 'd' character was found {count_d} times")
print(f"The 'e' character was found {count_e} times")
# (Continue this for all other characters...)

# Alternatively, return all counts if needed
counts = {
    'a': count_a, 'b': count_b, 'c': count_c, 'd': count_d, 'e': count_e, 'f': count_f,
    'g': count_g, 'h': count_h, 'i': count_i, 'j': count_j, 'k': count_k, 'l': count_l,
    'm': count_m, 'n': count_n, 'o': count_o, 'p': count_p, 'q': count_q, 'r': count_r,
    's': count_s, 't': count_t, 'u': count_u, 'v': count_v, 'w': count_w, 'x': count_x,
    'y': count_y, 'z': count_z
}

# You can return or print counts for further processing if needed
