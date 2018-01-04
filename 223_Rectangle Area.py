class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):

        s1 = (C-A)*(D-B)+(G-E)*(H-F)

        ver = max(0,min(C,G)-max(A,E))
        hor = max(0,min(D,H)-max(B,F))
        return s1-hor*ver
