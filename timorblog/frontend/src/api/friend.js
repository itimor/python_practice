import fetch from '@/utils/fetch';
import API from '@/config'

export function getfriendList() {
  return fetch({
    url: API.getfriendlist,
    method: 'get',
    params: {
      'limit':10,
      'active': true
    }
  });
}
