import { User } from './user.model';

export interface AuthState {
  user: User;
  authError: string;
  loading: boolean;
}
