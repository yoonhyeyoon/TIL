import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix


# 고객간의 유사도 행렬
def compute_sim(R):
    # user의 개수 / shape[1]은 영화의 개수
    num_users = R.shape[0]
    # 0이 아닌 곳은 모두 1로
    ones = csr_matrix((np.ones(R.nnz), (R.nonzero()[0], R.nonzero()[1])), shape=R.shape)
    # dense metrix로 만들기 위해 toarray : 내가 부여한 평점 * 너가 부여한 평점. 어차피 곱하면 한쪽이 0이면 0
    UbyU = (R * R.transpose()).toarray() # 분자
    # 고객간의 유사도 구하는 건데 자기자신은 당연히 0
    UbyU[range(num_users), range(num_users)] = 0
    
    sim = np.zeros((num_users, num_users))
    for i in range(num_users):
        # 나도 부여했고 너도 부여한 영화 
        both = ones[i].reshape(1, -1).multiply(ones)
        # 나도 부여했고 너도 부여한 영화에 i(u)번째 고객이 등록한 평점을 곱함 : ord = 루트
        norm_i = norm(both.multiply(R[i].reshape(1,-1)), ord=2, axis=1) # 분모(왼)
        # 나도 부여했고 너도 부여한 영화에 v번째 고객이 등록한 평점을 곱함
        norm_others = norm(both.multiply(R), ord=2, axis=1) # 분모(오)
        den = norm_i * norm_others #분모
        # 분모가 0이면 계산 자체가 안되니까 1로 바꿈 : 어차피 분자가 0이면 결과는 0
        den[den == 0] = 1
        sim[i] = UbyU[i] / den
    return sim


def predict(R, K):
    num_users = R.shape[0]
    num_items = R.shape[1]

    sim = compute_sim(R)
    # sorting한 index 저장
    topk = sim.argsort(axis=1)[:, -K:]

    # num_user * num_items 행렬을 만들고 모두 0인 행렬
    R_predicted = np.zeros((num_users, num_items))
    for i in range(num_users):
        # i번째 고객의 가장 유사한 고객들(top-K개)의 유사도
        weights = sim[i, topk[i]]
        for j in range(K):
            R_predicted[i] += weights[j] * R[topk[i,j]]
        R_predicted[i] /= weights.sum()
    return R_predicted

if __name__ == '__main__':
    R = csr_matrix(np.array([
        [1, 2, 0],
        [1, 0, 3],
        [3, 2, 1],
        [3, 2, 2],
        [1, 2, 2],
    ]))
    R_predicted = predict(R, 2)
