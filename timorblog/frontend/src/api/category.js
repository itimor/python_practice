import fetch from '@/utils/fetch';
import API from '@/config'

export function getcategoryList(query) {
  return fetch({
    url: API.getcategorylist,
    method: 'get',
    params: query
  });
}
